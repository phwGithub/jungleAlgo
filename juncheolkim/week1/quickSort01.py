# 내부분할 알고리즘.
# 추가 메모리를 사용하지 않는다.

# 피봇을 기준으로 배열 정렬
def partition(arr, start, end):
    pivot = arr[start]    # 좌측 끝단을 피봇 기준으로 한다. 피봇 기준을 어디로 하느냐에 따라서 시간복잡도가 달라진다. 
    left = start + 1 # 피봇 바로 다음부터
    right = end # 우측 끝 단부터
    done = False # while문 중단점
    while not done:
        while left <= right and arr[left] <= pivot: # 1번: 좌측에서 우측으로 움직이면서 피봇보다 큰 수를 찾을때까지 움직인다.
            left += 1
        while left <= right and pivot <= arr[right]: # 2번: 우측에서 좌측으로 움직이면서 피봇보다 작은 수를 찾을때까지 움진인다.
            right -= 1
        if right < left: # 1번과 2번이 만족하는데 만약 포인터가 서로 지나치면 while문을 중단한다.
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left] # 1번과 2번을 만족하고 중단이 되지 않는다면 해당 배열을 정렬한다.
    arr[start], arr[right] = arr[right], arr[start] # 위 while문이 끝나먄(정렬이 끝나면) 마지막 right(피봇보다 큰 수)와 피봇을 정렬한다.
    return right # 다음 피봇은 정렬 이후의 right가 된다.

# 퀵 소트 호출
def quick_sort(arr, start, end):
    if start < end:
        # 피봇 기준으로 정렬
        pivot = partition(arr, start, end)
        # 정렬된 배열의 피봇 기준 좌측 퀵 소트 호출
        quick_sort(arr, start, pivot - 1)
        #  정렬된 배열의 피봇 기준 우측 퀵 소트 호출
        quick_sort(arr, pivot + 1, end)
    return arr # 재귀를 통해 피봇기준으로 