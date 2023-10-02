#include "lists.h"

/**
 * check_cycle - Function checks if a linked list contains a cycle
 * @list: the linked list to be checked
 * Return: returns 1 if list has a cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *i = list;
	listint_t *j = list;

	if (!list)
	{
		return (0);
	}

	while (i && j && j->next)
	{
		i = i->next;
		j = j->next->next;

		if (i == j)
		{
			return (1);
		}
	}

	return (0);
}
