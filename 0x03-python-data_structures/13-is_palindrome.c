#include "lists.h"

/**
 * is_palindrome - A function that checks whether a linked list is a palindrome
 * @head: A double pointer to head of the linked list
 * Return: 0 if it is not palindrome 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slowpointer = *head, *fastpointer =  *head;
	listint_t *current = NULL, *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fastpointer != NULL && fastpointer->next != NULL)
	{
		fastpointer = fastpointer->next->next;
		temp = slowpointer->next;
		slowpointer->next = current;
		current = slowpointer;
		slowpointer = temp;
	}
	if (fastpointer != NULL)
	{
		slowpointer = slowpointer->next;
	}
	while (current != NULL && slowpointer != NULL)
	{
		if (current->n != slowpointer->n)
			return (0);
		current = current->next;
		slowpointer = slowpointer->next;
	}
	return (1);
}
