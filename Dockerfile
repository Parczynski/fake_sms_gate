FROM    node:20-alpine

RUN     apk add --no-cache python3 py3-pip

WORKDIR /app

COPY    package.json package-lock.json requirements.txt ./

RUN     npm i

RUN     pip install -r requirements.txt

COPY    . .

RUN     npm run build

RUN     chown -R node:node /app

USER    node

EXPOSE  3000

CMD     [ "python", "-m", "app.main" ]