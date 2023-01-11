#include "hash_tables.h"

/**
* hash_table_create - function that create a hash table
* @size: size of the hash table
* Returns: point to the hash table
*/

hash_table_t *hash_table_create(unsigned long int size);
{
	int i;
	hash_table_s *ht = (hash_table_s *) malloc(sizeof(hash_node_s));

	if (!ht)
	{
		return (NULL);
	}
	ht->size = size;
	ht->array = (hash_node_s **) calloc(size, sizeof(hash_node_s *));
	if (!ht->array)
	{
		free(ht);
		return (NULL);
	}
	for (i = 0; i < ht->size; i++)
		ht->array[i] = NULL;
	return (ht);
}
