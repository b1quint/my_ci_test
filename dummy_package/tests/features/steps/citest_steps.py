from behave import given, when, then

@given(u'I have a proper name')
def setp_impl(context):
    raise NotImplementedError(u'STEP: this is a given step')

@when(u'I am running the program')
def setp_impl(context):
    raise NotImplementedError(u'STEP: this is a when step')

@then(u'Greet as you are supposed to')
def setp_impl(context):
    raise NotImplementedError(u'STEP: this is a then step')
