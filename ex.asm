section .data
	a dd 10
	b dd 10
	msg db "%d and %d",10,0

section .text
	global main
	extern printf
main:	mov eax, a
	mov ebx, b
	push b
	push a
	push msg
	call printf
	add esp,12
