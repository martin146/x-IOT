from machine import Pin
import time
from modules.lora_E5 import LoRaE5
import modules.but_board as board

led = Pin(board.MOD_EN_PIN, Pin.OUT)

lora = LoRaE5(board.UART_RX_PIN, board.UART_TX_PIN, 9600)


def thread_core_0():
    while True:
        # lora.test_at()
        # lora.get_id()
        # lora.set_id('DevAddr', '32303C9E')
        # lora.get_version()
        # lora.send_ascii("Test", False)
        # lora.set_port(128)
        # lora.get_port()
        # lora.get_adr()
        # lora.set_adr(False)
        # lora.get_dr()
        # lora.set_dr(5)
        # lora.get_band_scheme()
        # lora.get_all_channels()
        # lora.get_channel(2)
        # lora.get_enabled_channels()
        # lora.get_power()
        # lora.set_power(10)
        # lora.get_power_map()
        # lora.get_ret_limit()
        # lora.get_rx2()
        # lora.set_rx2(869525000, 5)
        # lora.set_id('DevEui', '0004A30B00286CF6')
        # lora.set_id('DevAddr', '26011460')

        # lora.set_key('NWKSKEY', '2BB9329DB9D0497A4F1301C83D5D3C35')
        # lora.set_key('APPSKEY', 'A8AF3A28305A188FD86AE5E638746371')

        # lora.set_dr_band('EU868')
        # lora.set_mode('LWABP')
        # lora.set_dr(0)
        # lora.enable_channel(0)
        # lora.enable_channel(1)
        # lora.enable_channel(2)
        # lora.get_enabled_channels()
        # lora.set_port(55)
        # lora.set_counters(32, 32)
        # lora.set_etsi_duty_cycle(True)

        # lora.send_ascii('Hello')
        # lora.read_n_times(25)

        # lora.get_rx_delay()
        # lora.set_rx_delay('RX1', 1000)

        time.sleep(10)


thread_core_0()
