import { openai } from '@ai-sdk/openai'
import { convertToCoreMessages, CoreMessage, streamText } from 'ai'

// Allow streaming responses up to 30 seconds
export const maxDuration = 30

export async function POST(req: Request) {
	const { messages, initialData } = await req.json()

	console.log('messages', messages)
	console.log('initialData', initialData)

	const coreMessages: CoreMessage[] = [
		{
			role: 'system',
			content: `You are responsible for answering follow up questions based on previous analysis. Here is the previous analysis: ${initialData}`,
		},
		...convertToCoreMessages(messages),
	]

	const result = streamText({
		model: openai('gpt-4o'),
		messages: coreMessages,
	})

	return result.toDataStreamResponse()
}
