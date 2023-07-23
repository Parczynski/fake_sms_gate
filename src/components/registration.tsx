import { FC, FormEventHandler, useContext, useState } from 'react';
import styles from './registration.module.scss'
import { ProviderContext } from '../core/provider';

export const Registration: FC = () => {

	const { register } = useContext( ProviderContext )
	const [ phone, setPhone ] = useState( '' )

	const submit: FormEventHandler = (e) => {
		e.preventDefault()
		register( phone )
	}
	return (
		<>
			<form id={styles.registration} onSubmit={submit}>
				<label htmlFor="phone">Phone number:</label>
				<input type="tel" name="phone" id="phone" value={phone} onChange={(e) => setPhone(e.currentTarget.value)} maxLength={12} placeholder='+79000000000' />
				<button>Set Number</button>
			</form>
		</>
	)
}