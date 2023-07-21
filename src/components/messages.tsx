import { FC } from 'react';
import styles from './messages.module.scss'
export const Messages: FC = () => {
	return (
		<div id={styles.messages}>
			<div className="message">
				5012 - код подтверждения
			</div>
		</div>
	)
}