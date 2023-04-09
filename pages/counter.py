class Counter:
    pass_results = 0
    fail_results = 0

    @property
    def count_fail(self):
        return self.pass_results

    def add_fail(self):
        self.pass_results += 1
        return self.pass_results

    @property
    def count_pass(self):
        return self.fail_results

    def add_pass(self):
        self.fail_results += 1
        return self.fail_results
