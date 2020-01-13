
def test_calendar():
    # d_id정의
    device_id = "ce031713d239a82002"
    # 핸드폰을 연결한다.
    import uiautomator2 as u2
    d = u2.connect(device_id)
    # 정상적으로 연결된다.
    print(d.alive)
    assert d.alive, "디바이스가 정상적으로 연결되지 않았습니다."

    # 캘린더 앱을 실행한다.
    app_package = "com.samsung.android.calendar"
    d.app_start(app_package)
    # 프로그램이 정상적으로 수행된다.
    pid = d.app_wait(app_package, timeout=20.0)
    if not pid:
        print("com.example.android is not running")
        assert False, f"{app_package}가 정상적으로 수행되지 않았습니다."

    # 할일이름값을 정의한다.
    import time
    task_name = f"{time.time()}_할일"
    # 새로운 일정을 등록한다.
    # 일정등록 버튼 클릭
    d.xpath('//*[@resource-id="com.samsung.android.calendar:id/floating_action_button"]').click()
    # 일정 제목에 내용 입력
    d.xpath('//*[@resource-id="com.samsung.android.calendar:id/title"]').set_text(task_name)
    # 저장 버튼 클릭
    d.xpath('//*[@resource-id="com.samsung.android.calendar:id/action_done"]').click()

    # 일정이 정상적으로 등록되었는지 확인한다.
    # 더보기 버튼 클릭
    d(text="보기 방식").right(className='android.widget.FrameLayout').click()
    # 검색 버튼 클릭
    d.xpath('//android.widget.ListView/android.widget.LinearLayout[1]').click()
    # task_name으로 검색
    d(resourceId="android:id/search_src_text").send_keys(task_name)
    # task_name element존재 여부 확인
    d(resourceId="com.samsung.android.calendar:id/title", text=task_name).exists()
