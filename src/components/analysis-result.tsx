'use client'

import ReactMarkdown from 'react-markdown'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

interface AnalysisResultProps {
	result: string
}

export default function AnalysisResult({ result }: AnalysisResultProps) {
	return (
		<Card className='mt-8 bg-background/90 border-none shadow-lg'>
			<CardHeader>
				<CardTitle className='text-xl'>Analysis Results</CardTitle>
			</CardHeader>
			<CardContent>
				<div className='prose prose-invert max-w-none'>
					<ReactMarkdown>{result}</ReactMarkdown>
				</div>
			</CardContent>
		</Card>
	)
}
