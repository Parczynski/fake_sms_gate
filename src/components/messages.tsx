import { FC, useContext } from 'react';
import styles from './messages.module.scss'
import { ProviderContext } from '../core/provider';
export const Messages: FC = () => {

	const { messages } = useContext(ProviderContext)

	

	return (
		<div id={styles.messages}>
			{
				messages.map( (msg,index) => <div key={msg.id} className={`${styles.message} ${index===0?'animate__animated animate__bounceInRight':''}`}>{msg.content}</div> )
			}
		</div>
	)
}