GET_CHARACTERS = """
  SELECT * FROM charactercreator_character;
"""

EXAMPLE = """
  SELECT * 
  FROM charactercreator_character
  WHERE character_id > 50
  AND character_id < 200;
"""

EXAMPLE_OF_SUBQUERY = """
  SELECT name, COUNT(item_id) AS total_character_items
  FROM (SELECT *
  FROM  charactercreator_character as characters
  INNER JOIN charactercreator_character_inventory as inventory
  ON characters.character_id = inventory.character_id)
  GROUP BY name
  ORDER BY total_character_items DESC;
"""
