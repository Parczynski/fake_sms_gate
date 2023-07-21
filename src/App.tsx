import { Messages } from './components/messages'
import { Registration } from './components/registration'
import { SMSProvider } from './core/provider'

function App() {
  


  return (
    <SMSProvider>
      <div className="container">
        <Registration />
        <Messages />
      </div>
    </SMSProvider>
  )
}

export default App
