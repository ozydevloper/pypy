from playwright.sync_api import sync_playwright
from time import sleep

URL = ''

NAMA_MENU = "MYMAPS1"

NAMA_SPREADSHET = 'MYMAPS'

with sync_playwright() as play:
    browser = play.chromium.launch_persistent_context(channel='chrome', headless=False, user_data_dir="C:\\ICRMAUTO")
    page = browser.new_page()
    page.goto(URL)
    page.wait_for_load_state('networkidle')


    menu = page.get_by_text(text=NAMA_MENU)
    parent = menu.evaluate_handle("el => el.parentElement.childNodes[2]")
    opsi_menu = parent.as_element().click()

    opsi_Impor_ulang_dan_gabungkan = page.get_by_role(role='menuitem',name="Impor ulang dan gabungkan")
    opsi_Impor_ulang_dan_gabungkan.scroll_into_view_if_needed()
    opsi_Impor_ulang_dan_gabungkan.click()

    opsi_Impor_ulang = page.get_by_role("menuitem", name="Impor ulang ►")
    opsi_Impor_ulang.click()

    opsi_ganti_semua = page.get_by_role(role='menuitem',name="Ganti semua item")
    opsi_ganti_semua.click()
    sleep(2)

    picker = page.query_selector('div.picker-dialog-content')
    child = picker.evaluate_handle("el => el.childNodes[0]")
    frame = child.as_element().content_frame()
    element_google_drive = frame.get_by_text(text="Google Drive")
    element_google_drive.click()

    element_terbaru = frame.get_by_text(text="Terbaru")
    element_terbaru.click()

    element_mymaps = frame.get_by_text(text=f"{NAMA_SPREADSHET}")
    element_mymaps.click()

    element_sisipkan = frame.get_by_text(text="Sisipkan")
    element_sisipkan.click()
    page.wait_for_load_state('networkidle')

    parent_buat_atur_warna = menu.evaluate_handle("el => el.parentElement.parentElement")
    div_warna = parent_buat_atur_warna.query_selector('//*[@id="ly1-layer-items-container"]')
    div_warna.hover()
    sleep(1)

    icon_ember = div_warna.evaluate_handle("el => el.childNodes[0].childNodes[2]")
    icon_ember.click()

    warna_kuning = page.locator('//div[@data-tooltip="RGB (255, 234, 0)"]')
    warna_kuning.click()

    logo_rumah = page.locator('//*[@id=":p"]/div/div/div')
    logo_rumah.click()

    close_warna = page.locator('//*[@id="stylepopup-close"]')
    close_warna.click()
    sleep(5)
    

    