

# Generated at 2024-03-18 09:18:37.436574
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    assert test_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not test_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    test_module = LinuxAcademyIE()
    assert test_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not test_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print("All tests passed!")


# Generated at 2024-03-18 09:18:42.396078
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True
    assert single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154') == False

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == False
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True


# Generated at 2024-03-18 09:18:49.703271
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract_info(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test

# Generated at 2024-03-18 09:18:58.293660
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    single_video_info = single_video.extract('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['ext'] == 'mp4'
    assert single_video_info['title'] == 'What Is Data Science'
    assert 'description' in single_video_info
    assert single_video_info['timestamp'] == 1607387907
    assert single_video_info['upload_date'] == '20201208'
    assert single_video_info['duration'] == 304

    # Test case for a course
    course = LinuxAcademyIE()

# Generated at 2024-03-18 09:19:06.750825
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a course with a single video
    single_video = LinuxAcademyIE()
    single_video._set_downloader(None)
    test_url_single_video = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    single_video_info = single_video.extract(test_url_single_video)
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['ext'] == 'mp4'
    assert single_video_info['title'] == 'What Is Data Science'
    assert 'description' in single_video_info
    assert single_video_info['timestamp'] == 1607387907
    assert single_video_info['upload_date'] == '20201208'
    assert single_video_info['duration'] == 304

    # Test case for a course module with multiple videos
    course_module = LinuxAcademyIE()
    course_module._set

# Generated at 2024-03-18 09:19:15.044268
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:19:21.751139
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True
    assert single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154') == False

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == False
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True

    # Test case for invalid URL
    invalid_url = LinuxAcademyIE()
    assert invalid_url.suitable('https://example.com/path/to/video') == False

# Generated at 2024-03-18 09:19:30.194561
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:19:38.422749
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print('All tests passed!')


# Generated at 2024-03-18 09:19:45.261126
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_id = '7971-2'
    test_video_title = 'What Is Data Science'
    test_video_description_md5 = 'c574a3c20607144fb36cb65bdde76c99'
    test_video_timestamp = 1607387907
    test_video_upload_date = '20201208'
    test_video_duration = 304
    test_video_info = test_video.extract_info(test_video_url)
    assert test_video_info['id'] == test_video_id
    assert test_video_info['title'] == test_video_title
    assert hashlib.md5(test_video_info['description'].encode('utf-8')).hexdigest() == test_video_description_md5
    assert test_video_info

# Generated at 2024-03-18 09:20:31.563578
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a valid URL
    valid_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    extractor = LinuxAcademyIE()
    assert extractor.suitable(valid_url), "LinuxAcademyIE should recognize the URL"

    # Test case for an invalid URL
    invalid_url = 'https://invalid.linuxacademy.com/course/1234'
    assert not extractor.suitable(invalid_url), "LinuxAcademyIE should not recognize the URL"

    # Test case for extracting ID
    chapter_id, lesson_id, course_id = extractor._match_id(valid_url)
    assert chapter_id == '7971', "Extracted chapter ID should be '7971'"
    assert lesson_id == '2', "Extracted lesson ID should be '2'"
    assert course_id is None, "Extracted course ID should be None for this URL"



# Generated at 2024-03-18 09:20:38.270468
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print("All tests passed!")


# Generated at 2024-03-18 09:20:45.762495
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a course with a single video
    single_video = LinuxAcademyIE()
    single_video._real_initialize()
    single_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    single_video_info = single_video.extract(single_video_url)
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['title'] == 'What Is Data Science'
    assert 'formats' in single_video_info

    # Test case for a course module with multiple videos
    course_module = LinuxAcademyIE()
    course_module._real_initialize()
    course_module_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    course_module_info = course_module.extract(course_module_url)
    assert course_module_info['_type'] == 'playlist'
    assert course_module_info['id'] == '154'
   

# Generated at 2024-03-18 09:20:55.137602
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:21:09.198215
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course
    course = LinuxAcademyIE()
    assert course.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print('All tests passed!')


# Generated at 2024-03-18 09:21:15.430116
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    single_video_info = single_video.extract('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['ext'] == 'mp4'
    assert single_video_info['title'] == 'What Is Data Science'
    assert 'description' in single_video_info
    assert single_video_info['timestamp'] == 1607387907
    assert single_video_info['upload_date'] == '20201208'
    assert single_video_info['duration'] == 304

    # Test case for a course module
    course_module = LinuxAcademyIE()


# Generated at 2024-03-18 09:21:23.945406
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:21:34.110192
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a course lesson
    test_lesson = LinuxAcademyIE()
    lesson_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    lesson_info = test_lesson.extract_info(lesson_url)
    assert lesson_info['id'] == '7971-2'
    assert lesson_info['ext'] == 'mp4'
    assert lesson_info['title'] == 'What Is Data Science'
    assert 'description' in lesson_info
    assert lesson_info['timestamp'] == 1607387907
    assert lesson_info['upload_date'] == '20201208'
    assert lesson_info['duration'] == 304

    # Test case for a course module
    test_module = LinuxAcademyIE()
    module_url = 'https://linuxacademy.com/cp/modules/view/id/154'

# Generated at 2024-03-18 09:21:40.462348
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True
    assert single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154') == False

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == False
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True

    # Test case for invalid URL
    invalid_url = LinuxAcademyIE()
    assert invalid_url.suitable('https://example.com/path/to/video') == False


# Generated at 2024-03-18 09:21:46.679897
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print('All tests passed!')


# Generated at 2024-03-18 09:23:12.377485
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    single_video_info = single_video.extract_info('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['ext'] == 'mp4'
    assert single_video_info['title'] == 'What Is Data Science'
    assert 'description' in single_video_info
    assert single_video_info['timestamp'] == 1607387907
    assert single_video_info['upload_date'] == '20201208'
    assert single_video_info['duration'] == 304

    # Test case for a course
    course = LinuxAcademyIE()
   

# Generated at 2024-03-18 09:23:21.063742
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True
    assert single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154') == False

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == False
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True

    # Test case for invalid URL
    invalid_url = LinuxAcademyIE()
    assert invalid_url.suitable('https://example.com/path/to/video') == False


# Generated at 2024-03-18 09:23:29.008801
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:23:39.879492
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print("All tests passed!")


# Generated at 2024-03-18 09:23:46.882193
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    single_video_info = single_video.extract('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['title'] == 'What Is Data Science'
    assert single_video_info['duration'] == 304

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    course_module_info = course_module.extract('https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2024-03-18 09:23:54.285263
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')


# Generated at 2024-03-18 09:24:01.507409
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:24:12.006347
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:24:19.493246
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    assert test_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    test_info = test_video.extract_info('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert test_info['id'] == '7971-2'
    assert test_info['ext'] == 'mp4'
    assert test_info['title'] == 'What Is Data Science'
    assert 'description' in test_info
    assert test_info['timestamp'] == 1607387907
    assert test_info['upload_date'] == '20201208'
    assert test_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()

# Generated at 2024-03-18 09:24:27.627344
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    single_video_info = single_video.extract_info('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert single_video_info['id'] == '7971-2'
    assert single_video_info['ext'] == 'mp4'
    assert single_video_info['title'] == 'What Is Data Science'
    assert 'description' in single_video_info
    assert 'timestamp' in single_video_info
    assert 'upload_date' in single_video_info
    assert 'duration' in single_video_info

    # Test case for a course

# Generated at 2024-03-18 09:27:06.166846
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    assert test_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    test_info = test_video.extract_info('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert test_info['id'] == '7971-2'
    assert test_info['ext'] == 'mp4'
    assert test_info['title'] == 'What Is Data Science'
    assert 'description' in test_info
    assert test_info['timestamp'] == 1607387907
    assert test_info['upload_date'] == '20201208'
    assert test_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()

# Generated at 2024-03-18 09:27:11.406397
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print("All tests passed!")


# Generated at 2024-03-18 09:27:19.584612
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True
    assert single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154') == False

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == False
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True

    # Test case for invalid URL
    invalid_url = LinuxAcademyIE()
    assert invalid_url.suitable('https://example.com/path/to/video') == False


# Generated at 2024-03-18 09:27:27.246296
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    assert test_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    test_info = test_video.extract_info('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert test_info['id'] == '7971-2'
    assert test_info['ext'] == 'mp4'
    assert test_info['title'] == 'What Is Data Science'
    assert 'description' in test_info
    assert test_info['timestamp'] == 1607387907
    assert test_info['upload_date'] == '20201208'
    assert test_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()

# Generated at 2024-03-18 09:27:36.052299
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a valid URL
    valid_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    extractor = LinuxAcademyIE()
    assert extractor.suitable(valid_url), "LinuxAcademyIE should recognize the URL"

    # Test case for an invalid URL
    invalid_url = 'https://example.com/invalid'
    assert not extractor.suitable(invalid_url), "LinuxAcademyIE should not recognize the URL"

    # Test case for extracting ID
    expected_id = '7971-2'
    extracted_id = extractor._match_id(valid_url)
    assert extracted_id == expected_id, f"Extracted ID should be {expected_id}, got {extracted_id}"

    print("All tests passed.")


# Generated at 2024-03-18 09:27:44.907657
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')

    print("All tests passed!")


# Generated at 2024-03-18 09:27:52.472340
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a valid URL with chapter and lesson IDs
    test_instance_1 = LinuxAcademyIE('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert test_instance_1.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not test_instance_1.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Test case for a valid URL with a course ID
    test_instance_2 = LinuxAcademyIE('https://linuxacademy.com/cp/modules/view/id/154')
    assert test_instance_2.suitable('https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2024-03-18 09:28:00.657625
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    single_video = LinuxAcademyIE()
    assert single_video.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True
    assert single_video.suitable('https://linuxacademy.com/cp/modules/view/id/154') == False

    # Test case for a course module
    course_module = LinuxAcademyIE()
    assert course_module.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == False
    assert course_module.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True


# Generated at 2024-03-18 09:28:10.739655
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    # Test case for a single video
    test_video = LinuxAcademyIE()
    test_video_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_video_info = test_video.extract(test_video_url)
    assert test_video_info['id'] == '7971-2'
    assert test_video_info['ext'] == 'mp4'
    assert test_video_info['title'] == 'What Is Data Science'
    assert 'description' in test_video_info
    assert test_video_info['timestamp'] == 1607387907
    assert test_video_info['upload_date'] == '20201208'
    assert test_video_info['duration'] == 304

    # Test case for a course
    test_course = LinuxAcademyIE()
    test_course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    test_course

# Generated at 2024-03-18 09:28:18.637899
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():    ie = LinuxAcademyIE()

    # Test _VALID_URL pattern matching