'use client'

import { useState } from 'react'
import LoadingIndicator from './loading-indicator'
import AnalysisResult from './analysis-result'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { useChat } from 'ai/react'
import ReactMarkdown from 'react-markdown'

export default function CryptoAnalysis() {
	const [asset, setAsset] = useState('')
	const [state, setState] = useState<'processing' | 'completed' | null>(null)
	const [analyzeId, setAnalyzeId] = useState('')
	const [result, setResult] = useState('')
	const [initialData, setInitialData] = useState('')
	const { messages, input, handleInputChange, handleSubmit } = useChat({})

	const handleAssetSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault()

		if (!asset) {
			return alert('please spesify asset')
		}

		const res = await fetch(`http://localhost:5000/crypto-asset/${asset}`)
		const data = await res.json()
		setAnalyzeId(data.result)
		setState('processing')
	}

	const handleFollowUpSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		console.log({ initialData })
		handleSubmit(event, {
			body: {
				initialData,
			},
		})
	}

	const isLoading = state === 'processing'

	return (
		<Card className='max-w-3xl mx-auto backdrop-blur-lg bg-background/80 border-none shadow-lg'>
			<CardHeader>
				<CardTitle className='text-2xl'>Enter Crypto Asset</CardTitle>
			</CardHeader>
			<CardContent>
				<form onSubmit={handleAssetSubmit} className='space-y-4'>
					<div className='flex items-center space-x-2'>
						<Input
							type='text'
							value={asset}
							onChange={(e) => setAsset(e.target.value)}
							placeholder='Enter crypto asset (e.g., BTC, ETH)'
							name='asset'
							required
							className='flex-grow bg-background/50'
						/>
						<Button
							type='submit'
							disabled={isLoading}
							className='bg-gradient-to-r from-blue-500 to-purple-600 text-white'
						>
							{isLoading ? 'Analyzing...' : 'Analyze'}
						</Button>
					</div>
				</form>

				{isLoading && (
					<LoadingIndicator
						asset={asset}
						analyzeId={analyzeId}
						setState={setState}
						setResult={setResult}
						setInitialData={setInitialData}
					/>
				)}

				{!isLoading && result && (
					<>
						<AnalysisResult result={result} />

						<div>
							{messages.map((m) => (
								<div key={m.id} className='whitespace-pre-wrap'>
									{m.role === 'user' ? 'User: ' : 'AI: '}
									<div>
										<ReactMarkdown>{m.content}</ReactMarkdown>
									</div>
								</div>
							))}

							<form onSubmit={handleFollowUpSubmit} className='space-y-4 mt-8'>
								<Input
									type='text'
									value={input}
									onChange={handleInputChange}
									placeholder='Ask a follow-up question about the analysis'
									className='bg-background/50'
								/>
								<Button
									type='submit'
									className='w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white'
								>
									Ask Follow-up
								</Button>
							</form>
						</div>
					</>
				)}
			</CardContent>
		</Card>
	)
}
