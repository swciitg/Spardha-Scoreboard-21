FROM node:14-alpine AS builder
ENV NODE_ENV production
# Add a work directory
WORKDIR /app
# Cache and Install dependencies
COPY package.json .
COPY package-lock.json ./
RUN npm ci --silent
COPY . .
COPY .env* ./
RUN npm run build

FROM node:14-alpine AS prod
WORKDIR /app
COPY --from=builder /app/build ./build
RUN npm install -g serve
RUN mv ./build/static ./build/spardha

