import CryptoAnalysis from '@/components/crypto-analysis'

export default function Home() {
	return (
		<>
			<div className='flex items-center justify-center mb-8'>
				<h1 className='text-4xl mt-5 font-bold text-center bg-gradient-to-r from-blue-400 to-purple-600 text-transparent bg-clip-text'>
					✨ CryptoLens
				</h1>
			</div>
			<CryptoAnalysis />
		</>
	)
}
