import cv2

# Wymiary i pozycje początkowe kadru
frame_width = 800
frame_height = 800
start_position = (600, 100)

# Pozycja końcowa
end_position = (1200, 1200)

# Wczytanie pliku wideo
video_capture = cv2.VideoCapture('eoslena.mp4')

# Utworzenie obiektu VideoWriter do zapisu wideo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output.mp4', fourcc, 30, (frame_width, frame_height))

# Pętla przetwarzająca każdą klatkę wideo
while True:
    # Wczytanie kolejnej klatki
    ret, frame = video_capture.read()
    if not ret:
        break
    
    # Kadrowanie obszaru
    cropped_frame = frame[start_position[1]:start_position[1]+frame_height, 
                          start_position[0]:start_position[0]+frame_width]

    # Wyświetlenie kadrowanego obszaru
    cv2.imshow('Cropped Frame', cropped_frame)
    
    # Przesuwanie kadrowanego obszaru do pozycji końcowej
    start_position = (start_position[0] + 1, start_position[1] + 1)  # Przykładowe przesunięcie, można dostosować
    
    # Zapisanie kadrowanego obszaru do wynikowego pliku wideo
    output_video.write(cropped_frame)
    
    # Przerwanie pętli po osiągnięciu pozycji końcowej
    if start_position == end_position:
        break
    
    # Przerwanie pętli po naciśnięciu klawisza 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zwolnienie obiektów i zakończenie
video_capture.release()
output_video.release()
cv2.destroyAllWindows()

