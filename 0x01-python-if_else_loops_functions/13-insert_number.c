#include "lists.h"
/**
 * insert_node - function that inserts an element into a sorted linked list
 * @head: A double pointer to the head of the list
 * @n: number to insert
 * Return: new address of new node or Null if failed
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *current;
	listint_t *temp;

	if (head == NULL)
		return (NULL);
	current = *head;
	temp = malloc(sizeof(listint_t));
	if (!temp)
	{
		return (NULL);
	}
	temp->n = n;
	temp->next = NULL;
	if (current == NULL || current->n > n)
	{
		temp->next = *head;
		*head = temp;
		return (*head);
	}
	while (current->next != NULL && current->next->n < n)
	{
		current =  current->next;
	}
	temp->next = current->next;
	current->next = temp;
	return (temp);
}
