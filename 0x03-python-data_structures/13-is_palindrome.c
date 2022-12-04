#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *f;
	listint_t *s;

	f = list;
	s = list;
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
/**
* is_palindrome - Checks if a linked list is a palindrome
* @head: the head of the linked list
* Return: Returns 1 it is and 0 if it is not
*/

int is_palindrome(listint_t **head)
{
	int *list_vals;
	listint_t *f;
	int i, j;

	if (!head || (*head)->next == NULL)
		return (1);
	if (check_cycle(*head))
		return (1);
	list_vals = (int *)malloc(sizeof(int) * 1);
	if (list_vals == NULL)
	{
		free(list_vals);
		return (1);
	}

	f = *head;

	for (i = 0; f != NULL; i++)
	{
		list_vals[i] = f->n;
		f = f->next;
		if (f != NULL)
			list_vals = realloc(list_vals, sizeof(int) * i + 2);
	}
	i--;
	for (j = 0; i > 0; j++, i--)
	{
		if (list_vals[j] != list_vals[i])
		{
			free(list_vals);
			return (0);
		}
	}
	free(list_vals);
	return (1);
}
