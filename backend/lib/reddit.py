import time
from icecream import ic
from lib.env import env
import praw
import json
from lib.ai import get_ai_completions
from prawcore.exceptions import Forbidden, NotFound, RequestException
from requests.exceptions import HTTPError

client_id = env.get('REDDIT_CLIENT_ID')
client_secret = env.get('REDDIT_CLIENT_SECRET')
user_agent = env.get('REDDIT_APP_NAME')

reddit = praw.Reddit(
    client_id=client_id, 
    client_secret=client_secret, 
    user_agent=user_agent
)

def generate_subreddits(asset_name):
    system_prompt = "You are an expert at analyzing Reddit content to understand trends, topics, and communities related to stocks and cryptocurrencies. Your expertise enables you to identify the most relevant subreddits for specific assets."

    user_prompt = f"""
Generate a list of subreddits without r/ prefix that are relevant for the given asset. The output should include subreddits where discussions about this asset frequently occur or where users interested in this asset might engage. These subreddits will be used for sentiment analysis.

Input:

Asset: {asset_name}

Please return the response in this JSON format:
{{
    "subreddits": [] 
}}
"""
    
    return json.loads(get_ai_completions(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1,
        response_format={"type": "json_object"}
    ))
    


def fetch_subreddits(subreddits, asset_name, update_status):
    all_text = []
    failed_subreddits = []
    
    for subreddit in subreddits:
        # time.sleep(1)
        time.sleep(0.1)
        ic(f"Fetching from r/{subreddit}...")
        
        try:
            # top post for the week limited to just 1
            subreddit_instance = reddit.subreddit(subreddit)
            posts = subreddit_instance.search(query=asset_name, limit=10, time_filter='week')
            
            for post in posts:
                title = post.title
                all_text.append(title)
                
                try:
                    # controls the "Morecomments" object to load more comments
                    post.comments.replace_more(limit=3)
                    comments_array = post.comments[:2]
                    
                    for comment in comments_array:
                        body = comment.body
                        ic(subreddit, title)
                        ic(body)
                        all_text.append(body)
                        update_status('Fetching Subreddits Data', 'processing', body)
                                            
                except (Forbidden, NotFound, RequestException, HTTPError) as comment_error:
                    ic(f"Error fetching comments from r/{subreddit}: {str(comment_error)}")
                    continue
                    
        except (Forbidden, NotFound, RequestException, HTTPError) as subreddit_error:
            ic(f"Error accessing r/{subreddit}: {str(subreddit_error)}")
            failed_subreddits.append(subreddit)
            continue
            
    if failed_subreddits:
        ic(f"Failed to fetch from subreddits: {', '.join(failed_subreddits)}")
        
    return ' '.join(all_text) if all_text else "No data could be retrieved"

