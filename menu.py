class Menu():

    def __init__(self, base_object):
        # TODO(parth): validate that this array is of the right format
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
    valid = True

    # Validate leaf items
    if not is_root and not menu_item.get('description'):
	valid = False
	errors.append("Menu item needs text")

    # Check children
    if menu_item.get('children'):
	for child in menu_item['children']:
	    valid, child_errors = _validate_menu_item(child)
	    errors.extend(child_errors)
    return valid, errors
