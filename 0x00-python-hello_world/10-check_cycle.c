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
	while (_list && _list2->next)
	{
		_list = _list->next->next;
		_list2 = _list2->next;
		if (_list == _list2)
		{
			return (1);
		}
	}
	return (0);
}
