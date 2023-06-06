#include "lists.h"

/**
 * check_cycle - check if a linked list is a cycle
 * @list: start of the list
 *
 * Return: return 1 on sucess
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list->next;
	if (!list || !list->next)
		return (0);
	while (hare != NULL && hare->next != NULL)
	{
		if (hare == tortoise)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
