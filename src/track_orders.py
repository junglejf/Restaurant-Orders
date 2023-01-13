class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []
        self.days = set()

    def __str__(self):
        return f"Dict {self}"

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dishs = {}
        name, dish = 0, 1
        for order in self.orders:
            if order[name] == customer:
                dishs[order[dish]] = 1 if order[dish] not in dishs else(
                    dishs[order[dish]] + 1)

        return max(dishs, key=dishs.get)

    def get_never_ordered_per_customer(self, customer):
        name, dish = 0, 1
        all_dishs, customer_dish = set(), set()
        for order in self.orders:
            all_dishs.add(order[dish])
            if order[name] == customer:
                customer_dish.add(order[dish])
        return all_dishs - customer_dish

    def get_days_never_visited_per_customer(self, customer):
        name, day = 0, 2
        all_days, customer_day = set(), set()
        for order in self.orders:
            all_days.add(order[day])
            if order[name] == customer:
                customer_day.add(order[day])
        return all_days - customer_day

    def count_days_frequency(self):
        day, days = 2, {}
        for order in self.orders:
            days[order[day]] = 1 if order[day] not in days else(
                days[order[day]] + 1)
        self.days = days

    def get_busiest_day(self):
        self.count_days_frequency()
        return max(self.days, key=self.days.get)

    def get_least_busy_day(self):
        self.count_days_frequency()
        return min(self.days, key=self.days.get)
