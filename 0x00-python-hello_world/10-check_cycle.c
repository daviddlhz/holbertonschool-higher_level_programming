#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check the cycle in the singly linked list
 * @list: arguments input
 * Return: 0 if no cycle or 1 if its a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *_list =  list;
	listint_t *_list2 = list;

	if (list == NULL)
		return (0);
	while (1)
	{
		_list = _list->next;
		_list2 = _list2->next->next;
		if (_list->next == NULL || _list2->next->next == NULL)
			return (0);
		else if  (_list->next == _list2->next->next)
			return (1);
	}
	return (0);
}
