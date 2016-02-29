class Menu():

    def __init__(self, base_object):
        self.content = base_object


    def validate(self):
    	valid = True
    	errors = []
    	if not self.content.get('children'):
    	    return False, ["You're menu must have something in it!"]
    	valid, errors = _validate_menu_item(self.content, is_root=True)
    	return valid, errors


def _validate_menu_item(menu_item, is_root=False):
    errors = []
    our_valid = True

    # Validate leaf items
    if not is_root and not menu_item.get('description') and not menu_item['description']:
    	our_valid = False
    	errors.append("Menu item needs text.")

    # Validate id
    if not menu_item.get('id'):
        raise Exception("Menu items must have an id")

    # Check children
    if menu_item.get('children'):
    	for child in menu_item['children']:
    	    child_valid, child_errors = _validate_menu_item(child)
            our_valid &= child_valid
    	    errors.extend(child_errors)
    return our_valid, list(set(errors))