package main

import (
	"bufio"
	"context"
	"fmt"
	"net"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

const (
	connHost = "0.0.0.0"
	connPort = "1337"
	connType = "tcp"
)

func main() { // Used to stablish connections with the clients (not part of the challenge)
	fmt.Println("Starting " + connType + " server on " + connHost + ":" + connPort)
	l, err := net.Listen(connType, connHost+":"+connPort)
	if err != nil {
		fmt.Println("Error listening: ", err.Error())
		os.Exit(1)
	}
	defer l.Close()

	for {
		conn, err := l.Accept()
		if err != nil {
			continue
		}

		fmt.Println("Client " + conn.RemoteAddr().String() + " connected.")

		go minConnection(conn)
		go handleConnection(conn)
		defer conn.Close()
	}
}

func minConnection(conn net.Conn) {
	time.Sleep(600 * time.Second)
	conn.Close()
}

type LocalShell struct{}

func (_ LocalShell) Execute(ctx context.Context, cmd string) ([]byte, error) {
	wrapperCmd := exec.CommandContext(ctx, "bash", "-c", cmd)
	return wrapperCmd.Output()
}

func handleConnection(conn net.Conn) {
	conn.Write([]byte("CALCULATOR\n"))
	for {
		conn.Write([]byte("\nOperation: "))
		buffer, err := bufio.NewReader(conn).ReadBytes('\n')
		if err != nil {
			conn.Close()
			return
		}
		op := string(buffer[:len(buffer)-1]) 
        firewall := []string{" ", "`", "$", "&", "|", ";", ">"}
		for _, v := range firewall {
			opL1 := len(op)
			op = strings.ReplaceAll(op, v, "")
			opL2 := len(op)
			if opL1 > opL2 {
				conn.Write([]byte(strconv.Itoa(opL1-opL2) + "	'" + v + "' removed\n"))
			}
		}
		shell := LocalShell{}
		command := "echo $((" + op + "))" 
		output, _ := shell.Execute(context.Background(), command)
		fmt.Println(conn.RemoteAddr().String() + ": " + command + " " + string(output))
		conn.Write(output)
	}
}
