'use client'

import { useState, useEffect } from 'react'
import { doc, onSnapshot } from 'firebase/firestore'
import { db } from '@/lib/firebase'
import { LoaderCircle } from 'lucide-react'

interface LoadingIndicatorProps {
	asset: string
	analyzeId: string
	setState: React.Dispatch<React.SetStateAction<'processing' | 'completed' | null>>
	setResult: React.Dispatch<React.SetStateAction<string>>
	setInitialData: React.Dispatch<React.SetStateAction<string>>
}

export default function LoadingIndicator({
	asset,
	analyzeId,
	setState,
	setResult,
	setInitialData,
}: LoadingIndicatorProps) {
	const [steps, setSteps] = useState<{ taskName: string; status: string; details: string }[]>([])

	useEffect(() => {
		const docRef = doc(db, 'crypto_analysis', `${asset}_${analyzeId}`)
		const unsubscribe = onSnapshot(docRef, (doc) => {
			if (doc.exists()) {
				const data = doc.data()

				const { task_name, status, details, is_all_completed } = data

				setSteps((prev) => [
					...prev,
					{
						taskName: task_name,
						status,
						details,
					},
				])

				if (details) {
					setInitialData((prev) => prev + `Task: ${task_name}, Details: ${JSON.stringify(details)}\n`)
				}

				if (is_all_completed) {
					setState('completed')
					setResult(details)
				}
			}
		})

		return () => unsubscribe()
	}, [analyzeId])

	const lastStep = steps[steps.length - 1]?.taskName

	return (
		<div className='mt-8 space-y-4'>
			{/* <Progress value={progress} className='w-full bg-background/50' /> */}
			<div className='text-muted-foreground space-y-3'>
				<div className='flex'>
					{lastStep !== '' && <LoaderCircle className='animate-spin mr-3' />}
					{lastStep}
				</div>
				<details className='text-sm'>
					<summary>See details</summary>
					<div className='h-[300px] overflow-auto p-3 bg-muted mt-2 rounded-md'>
						{steps
							.filter((step) => step.details)
							.reverse()
							.map((step, idx) => (
								<div key={idx}>
									<div className='font-bold'>{step.taskName}</div>
									<div>{JSON.stringify(step.details)}</div>
								</div>
							))}
					</div>
				</details>
			</div>
		</div>
	)
}
