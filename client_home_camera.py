from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.video import Video
import cv2
import base64
import requests

class HomeMonitorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera()
        layout.add_widget(self.camera)
        self.player = Video(source='rtsp://localhost:8554/stream')
        layout.add_widget(self.player)
        return layout

    def start_monitoring(self):
        # Запуск видеопотока с камеры
        self.camera.open(0)
        self.player.play()

if __name__ == '__main__':
    HomeMonitorApp().run()
