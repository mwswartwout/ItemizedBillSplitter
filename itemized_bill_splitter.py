from typing import List
import math

class Item:
    def __init__(self, name: str, amount: float) -> None:
        self.name = name
        self.amount = amount
    
    def __str__(self) -> str:
        return '{ ' + self.name + ': ' + self.amount + ' }'
    
    def __repr__(self) -> str:
        return 'Item(' + self.name + ',' + str(self.amount) + ')'

class Bill:
    def __init__(self, items: List[Item], tax: float, tip: float) -> None:
        self.items = items
        self.tax = tax
        self.tip = tip
      
        self.names = [] 
        for item in items:
            assert item.amount > 0
            if item.name != "all":
                self.names.append(item.name)
        assert tax >= 0
        assert tip >= 0
        
    
    def getSplit(self) -> List[Item]:
        total = 0
        totals = {}
        
        for item in self.items:
            total += item.amount
            if item.name in totals:
                totals[item.name] += item.amount
            elif item.name == "all":
                for name in self.names:
                    if name in totals:
                        totals[name] += item.amount / len(self.names)
                    else:
                        totals[name] = item.amount / len(self.names)
            else:
                totals[item.name] = item.amount
        print(total)
        print(totals)
        
        percentages = {}
        for name, amount in totals.items():
            assert name not in percentages
            percentages[name] = amount / total
        print(percentages)
        
        total_percent = 0
        for percent in percentages.values():
            total_percent += percent
        assert total_percent == 1
        
        tip_amount = {}
        tax_amount = {}
        for name, percentage in percentages.items():
            assert name not in tip_amount
            assert name not in tax_amount
            
            tip_amount[name] = percentage * self.tip
            tax_amount[name] = percentage * self.tax
        print(tip_amount)
        print(tax_amount)
            
        final_amounts = {}
        for name, amount in totals.items():
            assert name in tip_amount
            assert name in tax_amount
            assert name not in final_amounts
            final_amounts[name] = amount + tip_amount[name] + tax_amount[name]
    
        calced_total = 0
        for amount in final_amounts.values():
            calced_total += amount
        print(calced_total)
        print(total + self.tax + self.tip)
        assert math.isclose(calced_total, total + self.tax + self.tip)
       
         
        return [Item(name, round(amount, 2)) for name, amount in final_amounts.items()]
        
def main():
    bill = Bill([Item('all', 18), Item('Kyle', 25), Item('Rachel', 25), Item('Scott', 25), Item('Tyler', 23), Item('Sarah', 18), Item('Matt', 68)],16.16,43.63)
    print(bill.getSplit()) 

if __name__ == "__main__":
    main()