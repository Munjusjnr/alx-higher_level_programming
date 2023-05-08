#include "lists.h"

/**
 * check_cycle - function that checks whether there is a cycle in a list
 * @list: A pointer to the linked list
 * Return: 1 if there is a cycle 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	ptr2 = ptr1 = list;
	while (ptr1->next && ptr1->next->next)
	{
		ptr2 = ptr2->next;
		ptr1 = ptr1->next->next;
		if (ptr2 == ptr1)
		{
			return (1);
		}
	}
	return (0);
}
