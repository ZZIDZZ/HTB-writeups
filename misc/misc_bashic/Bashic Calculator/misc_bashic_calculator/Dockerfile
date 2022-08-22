FROM golang:1.18-alpine as builder
WORKDIR /build
RUN go mod init bashic.htb/calculator
COPY src/main.go /build/main.go
RUN go build

FROM alpine:latest
EXPOSE 1337
RUN apk add --no-cache bash
RUN addgroup -S ctf && adduser -S ctf -G ctf
COPY challenge/flag.txt /
COPY --chown=root:root --from=builder /build/calculator /calculator
WORKDIR /home/ctf
USER ctf
CMD [ "/calculator" ]
