"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

from ibapi.object_implem import Object
from ibapi.common import UNSET_DOUBLE


class OrderState(Object):

    def __init__(self):
        self.status= ""

        self.initMarginBefore= ""
        self.maintMarginBefore= ""
        self.equityWithLoanBefore= ""
        self.initMarginChange= ""
        self.maintMarginChange= ""
        self.equityWithLoanChange= ""
        self.initMarginAfter= ""
        self.maintMarginAfter= ""
        self.equityWithLoanAfter= ""

        self.commission = UNSET_DOUBLE      # type: float
        self.minCommission = UNSET_DOUBLE   # type: float
        self.maxCommission = UNSET_DOUBLE   # type: float
        self.commissionCurrency = ""
        self.warningText = ""
        self.completedTime = ""
        self.completedStatus = ""

    def __str__(self):
        return f'{self.status}'
