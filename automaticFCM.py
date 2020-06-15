from pyfcm import FCMNotification

mApi_key = "AAAA5ZH8TEo:APA91bEwkLBs3nluSJXvy7ICS2NQoMKfXkdba86NrM_hP1rZdzTktRSMGQc_1cX8JeDgFpBoopOOoZCg4sEoeHzf_Qo2cwwJ-s7uX-wa4obk8OQVXgkjrHlECa_ghoJbWD_ny0xLknNY"
mToken = "985996741706"

push_service = FCMNotification(api_key=mApi_key)

message_title = "멧돼지 감지"
message_body = "멧돼지가 감지되었습니다."

result = push_service.notify_single_device(registration_id=mToken, message_title=message_title, message_body=message_body)
