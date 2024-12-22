// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getFirestore } from 'firebase/firestore'

// Your web app's Firebase configuration
const firebaseConfig = {
	apiKey: 'AIzaSyB2yg_YGR5lxJoupwQX79LRmnH0wnk8t04',
	authDomain: 'cryptolens-7c1ef.firebaseapp.com',
	projectId: 'cryptolens-7c1ef',
	storageBucket: 'cryptolens-7c1ef.firebasestorage.app',
	messagingSenderId: '752072484045',
	appId: '1:752072484045:web:ff58a617edd927c46cb584',
}

// Initialize Firebase
export const app = initializeApp(firebaseConfig)
export const db = getFirestore(app)
