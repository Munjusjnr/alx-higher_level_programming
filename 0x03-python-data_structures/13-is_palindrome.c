#include "lists.h"

/**
 * is_palindrome - A function that checks whether a linked list is a palindrome
 * @head: A double pointer to head of the linked list
 * Return: 0 if it is not palindrome 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slowpointer = *head, *fastpointer =  *head;
	listint_t *current = *head, *previous = NULL, *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fastpointer != NULL && fastpointer->next != NULL)
	{
		fastpointer = fastpointer->next->next;
		previous = slowpointer;
		slowpointer = slowpointer->next->next;
	}
	if (fastpointer != NULL)
	{
		slowpointer = slowpointer->next;
	}
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = current;
		current = slow;
		slow = next;
	}
	while (current != *head)
	{
		if (current->n != (*head)->n)
			return (0);
		current = current->next;
		*head = (*head)->next;
	}
	return (1);
}
