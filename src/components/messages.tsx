import { FC, useState } from 'react';
import styles from './messages.module.scss'
export const Messages: FC = () => {

	const [ messages ] = useState<Message[]>( [] )

	

	return (
		<div id={styles.messages}>
			{
				messages.map( (msg,index) => <div key={msg.id} className={`${styles.message} ${index===0?'animate__animated animate__bounceInRight':''}`}>{msg.content}</div> )
			}
		</div>
	)
}