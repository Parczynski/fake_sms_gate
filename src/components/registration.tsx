import { FC } from 'react';
import styles from './registration.module.scss'

export const Registration: FC = () => {

	return (
		<>
			<form id={styles.registration}>
				<input type="tel" name="phone" id="" maxLength={12} placeholder='phone number' />
				<button>Set Number</button>
			</form>
		</>
	)
}