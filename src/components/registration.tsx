import { FC } from 'react';
import styles from './registration.module.scss'

export const Registration: FC = () => {

	return (
		<form id={styles.registration}>
			<input type="tel" name="phone" id="" placeholder='phone number' />
			<button>Register Number</button>
		</form>
	)
}