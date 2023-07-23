FROM        node:20-alpine AS deps

WORKDIR     /app

COPY        package.json package-lock.json ./

RUN         npm ci



FROM        node:20-alpine AS builder

WORKDIR     /app

COPY        --from=deps /app/node_modules ./node_modules

COPY        . .

RUN         npm run build



FROM        python:3.11-alpine as runner

WORKDIR     /app

COPY        requirements.txt ./

RUN         pip install -r requirements.txt

COPY        --from=builder /app/dist ./dist

COPY        ./app ./app

COPY        ./__init__.py ./

EXPOSE      3000

CMD         [ "python", "-m", "app.main" ]