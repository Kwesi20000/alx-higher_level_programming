#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *i;

	i = malloc(sizeof(listint_t));
	if (i == NULL)
		return (NULL);
	i->n = number;

	if (node == NULL || node->n >= number)
	{
		i->next = node;
		*head = i;
		return (i);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	i->next = node->next;
	node->next = i;

	return (i);
}
