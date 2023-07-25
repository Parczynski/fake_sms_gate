import { FC, PropsWithChildren, createContext, useCallback, useState } from 'react';


type Context = {
	messages: Array<Message>
	register: ( phone: string ) => void
}


export const ProviderContext = createContext( { } as Context )

const PROVIDER_ENDPOINT = location.protocol === 'https'
	? `wss://${location.host}/ws`
	: `ws://${location.host}/ws`

let ws: WebSocket | undefined

let error_number = 0


export const SMSProvider: FC<PropsWithChildren> = ( {children}) => {

	const [ messages, setMessages ] = useState<Message[]>([])

	const register = useCallback( ( phone: string ) => {
		if( phone === '' ) {
			const message: Message = {
				id: `${error_number++}_error`,
				content: `The phone number is required`
			}
			setMessages( old => [ message, ...old ] )
			return	
		}

		if( ws !== undefined )
			ws.close()

		ws = new WebSocket(`${PROVIDER_ENDPOINT}?phone=${encodeURIComponent( phone )}`);

		ws.onmessage = function(event) {
			const message = JSON.parse( event.data ) as Message
			setMessages( old => [ message, ...old ] )
		};
	}, [setMessages] )

	return (
		<>
			<ProviderContext.Provider value={{messages, register}}>
				{children}
			</ProviderContext.Provider>
		</>
	)
}