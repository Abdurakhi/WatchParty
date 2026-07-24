from enum import Enum


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class RoomRole(str, Enum):
    OWNER = "owner"
    MODERATOR = "moderator"
    VIEWER = "viewer"


class RoomVisibility(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class PlaybackState(str, Enum):
    IDLE = "idle"
    PLAYING = "playing"
    PAUSED = "paused"
    BUFFERING = "buffering"
    ENDED = "ended"


class BrowserState(str, Enum):
    STARTING = "starting"
    READY = "ready"
    STOPPED = "stopped"
    ERROR = "error"


class BrowserControl(str, Enum):
    CLICK = "click"
    DOUBLE_CLICK = "double_click"
    MOUSE_MOVE = "mouse_move"
    MOUSE_DOWN = "mouse_down"
    MOUSE_UP = "mouse_up"
    SCROLL = "scroll"
    KEY_DOWN = "key_down"
    KEY_UP = "key_up"
    TYPE = "type"


class InvitationStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"


class VideoProvider(str, Enum):
    GENERIC = "generic"
    DIRECT_URL = "direct_url"
    GOOGLE_DRIVE = "google_drive"
    VK_VIDEO = "vk_video"
    YOUTUBE = "youtube"


class WebSocketEvent(str, Enum):
    CONNECT = "connect"
    DISCONNECT = "disconnect"

    JOIN_ROOM = "join_room"
    LEAVE_ROOM = "leave_room"

    PLAY = "play"
    PAUSE = "pause"
    SEEK = "seek"

    SYNC = "sync"

    CHAT = "chat"

    PING = "ping"
    PONG = "pong"

    ERROR = "error"


class CachePrefix(str, Enum):
    USER = "user"
    ROOM = "room"
    PLAYBACK = "playback"
    SESSION = "session"


APP_DESCRIPTION = (
    "Real-time collaborative watch party platform."
)

MAX_ROOM_NAME_LENGTH = 100

MAX_USERNAME_LENGTH = 32

MIN_PASSWORD_LENGTH = 8

MAX_MESSAGE_LENGTH = 4000

DEFAULT_PAGE_SIZE = 20

MAX_PAGE_SIZE = 100
