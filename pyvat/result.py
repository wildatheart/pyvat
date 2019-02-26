class VatNumberCheckResult(object):
    """Result of a VAT number validation check.

    :ivar is_valid:
        Boolean value indicating if the checked VAT number was deemed to be
        valid. ``True`` if the VAT number is valid, ``False`` if the VAT
        number is positively invalid or ``None`` if the validity is
        nondeterministic due to adverse conditions.
    :ivar log_lines:
        Check log lines.
    :ivar business_name: Optional business name retrieved for the VAT number.
    :ivar business_address: Optional address retrieved for the VAT number.
    """

    def __init__(self,
                 is_valid=None,
                 log_lines=None,
                 business_name=None,
                 business_address=None,
                 country_code_result=None,
                 vat_nr_result=None,
                 request_date=None):
        self.is_valid = is_valid
        self.log_lines = log_lines or []
        self.business_name = business_name
        self.business_address = business_address
        self.country_code_result = country_code_result
        self.vat_nr_result = vat_nr_result
        self.request_date = request_date
