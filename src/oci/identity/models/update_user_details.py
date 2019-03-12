# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateUserDetails(object):
    """
    UpdateUserDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateUserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateUserDetails.
        :type description: str

        :param email:
            The value to assign to the email property of this UpdateUserDetails.
        :type email: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateUserDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateUserDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'email': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'email': 'email',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._email = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateUserDetails.
        The description you assign to the user. Does not have to be unique, and it's changeable.


        :return: The description of this UpdateUserDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateUserDetails.
        The description you assign to the user. Does not have to be unique, and it's changeable.


        :param description: The description of this UpdateUserDetails.
        :type: str
        """
        self._description = description

    @property
    def email(self):
        """
        Gets the email of this UpdateUserDetails.
        The email you assign to the user. Has to be unique across the tenancy.


        :return: The email of this UpdateUserDetails.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UpdateUserDetails.
        The email you assign to the user. Has to be unique across the tenancy.


        :param email: The email of this UpdateUserDetails.
        :type: str
        """
        self._email = email

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateUserDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateUserDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateUserDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateUserDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateUserDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateUserDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateUserDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateUserDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
