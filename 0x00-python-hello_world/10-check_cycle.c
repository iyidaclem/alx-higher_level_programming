#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linkedlist
 * @list: pointer to head of list
 * Return: 0 if there no cycle or 1 is there is
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if (list != NULL)
		return (0);
	f = s = list;
	while (s != NULL)
	{
		s = s->next;
		f = s->next;
		if (s == f)
			return (1);
	}
	return (0);
}

