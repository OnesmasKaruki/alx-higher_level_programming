#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * ckeck_cycle - checks the presence of cycle
 * @lists: pointer to listint_t
 *
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *jump, *node;

	if (!list || !list->next)
		return (0);

	node = list;
	jump = list-.next;

	while (jump && jump->next && node && node->next)
	{
		if (jump == node)
			return (1);
		jump = jump->next->next;

		if (!jump)
			break;
		node = node->next;
	}
	return (0);
}
