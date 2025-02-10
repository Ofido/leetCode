def searchInsert(self, nums: list[int], target: int) -> int:
    if len(nums) == 1:  # valido se o tamanho é 1 valido se é maior ou menor
        return 0 if nums[0] >= target else 1
    half = len(nums) // 2  # pego a metade
    if nums[-1] < target:
        return len(nums)
    if nums[-1] == target:
        return len(nums) - 1
    if nums[half] == target:
        return half
    if nums[half] < target:  # valido se o target está antes ou depois da metade
        return (
            self.searchInsert(nums[half:], target) + half
        )  # chamo novamente passando a metade maior, o target e somar a metade
    return self.searchInsert(
        nums[:half], target
    )  # chamo novamente a metade menor, sem somar a matade pois está antes dela
