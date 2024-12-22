import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
	title: 'CryptoLens',
	description: 'AI-powered crypto asset technical, news, and Reddit sentiment analysis',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
	return (
		<html lang='en' className='dark'>
			<body className={`${inter.className} bg-background`}>
				<main className='min-h-screen bg-background text-foreground relative overflow-hidden'>
					<div className='absolute inset-0 bg-gradient-to-br from-purple-500/20 via-blue-500/20 to-pink-500/20 blur-3xl' />
					<div className='container mx-auto p-4'>{children}</div>
				</main>
			</body>
		</html>
	)
}
