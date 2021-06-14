import cv2

# 開啟影片檔案
cap = cv2.VideoCapture('test1.avi')

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
  ret, frame = cap.read()

  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  print(132)

cap.release()
cv2.destroyAllWindows()